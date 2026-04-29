import {
  ChangeDetectorRef,
  Component,
  ElementRef,
  inject,
  OnDestroy,
  OnInit,
  ViewChild,
} from '@angular/core';
import { FormsModule } from '@angular/forms';
import { ActivatedRoute } from '@angular/router';
import type { ECharts, EChartsCoreOption } from 'echarts/core';
import { combineLatest, Subscription } from 'rxjs';

import { AuthClientService } from '../../core/auth-client.service';
import { DashboardClientService } from '../../core/dashboard-client.service';
import {
  ContextoRedModel,
  DetalleInteraccionesModel,
  InteraccionesPorRedModel,
  InteraccionesTiempoModel,
  PerfilMetricasModel,
} from '../../core/models';
import { createChart, observeChartResize } from '../../shared/echarts-utils';
import {
  DEFAULT_RED_SOCIAL,
  RED_SOCIAL_OPTIONS,
  redSocialColor,
} from '../../shared/dashboard-utils';

@Component({
  selector: 'app-perfil-dashboard',
  imports: [FormsModule],
  templateUrl: './perfil-dashboard.html',
  styleUrl: './perfil-dashboard.scss',
})
export class PerfilDashboardComponent implements OnInit, OnDestroy {
  @ViewChild('timelineChart') private timelineChartRef?: ElementRef<HTMLDivElement>;
  @ViewChild('redChart') private redChartRef?: ElementRef<HTMLDivElement>;
  @ViewChild('detalleChart') private detalleChartRef?: ElementRef<HTMLDivElement>;

  readonly redOptions = RED_SOCIAL_OPTIONS;
  redSocial = DEFAULT_RED_SOCIAL;
  selectedEstudiante = '';
  metricas: PerfilMetricasModel | null = null;
  contextoRed: ContextoRedModel | null = null;
  detalleInteracciones: DetalleInteraccionesModel[] = [];
  interaccionesTiempo: InteraccionesTiempoModel[] = [];
  interaccionesPorRed: InteraccionesPorRedModel[] = [];
  isLoading = false;
  isPerfilPropio = true;
  errorMessage = '';

  private readonly activatedRoute = inject(ActivatedRoute);
  private readonly authService = inject(AuthClientService);
  private readonly changeDetector = inject(ChangeDetectorRef);
  private readonly dashboardService = inject(DashboardClientService);
  private charts: ECharts[] = [];
  private querySubscription?: Subscription;
  private resizeObservers: ResizeObserver[] = [];

  ngOnInit(): void {
    this.querySubscription = combineLatest([
      this.activatedRoute.paramMap,
      this.activatedRoute.queryParamMap,
    ]).subscribe(([routeParams, queryParams]) => {
      const routeEstudiante =
        routeParams.get('estudiante') ?? queryParams.get('estudiante');
      const sessionEstudiante = this.authService.getSession()?.estudiante ?? '';
      const nextEstudiante = routeEstudiante || sessionEstudiante;
      this.isPerfilPropio = nextEstudiante === sessionEstudiante;

      if (nextEstudiante !== this.selectedEstudiante) {
        this.selectedEstudiante = nextEstudiante;
        this.loadPerfil();
      }
    });
  }

  ngOnDestroy(): void {
    this.querySubscription?.unsubscribe();
    this.disposeCharts();
  }

  get estudiante(): string {
    return this.selectedEstudiante;
  }

  get etiquetaPerfil(): string {
    return this.isPerfilPropio ? 'Mi perfil' : 'Perfil consultado';
  }

  loadPerfil(): void {
    if (!this.estudiante) {
      return;
    }

    this.disposeCharts();
    this.isLoading = true;
    this.errorMessage = '';
    this.changeDetector.detectChanges();

    this.dashboardService.getPerfil(this.estudiante, this.redSocial).subscribe({
      next: (response) => {
        this.metricas = response.metricas;
        this.contextoRed = response.contexto_red;
        this.detalleInteracciones = response.detalle_interacciones;
        this.interaccionesTiempo = response.interacciones_tiempo;
        this.interaccionesPorRed = response.interacciones_por_red;
        this.isLoading = false;
        this.changeDetector.detectChanges();
        setTimeout(() => this.renderCharts());
      },
      error: () => {
        this.errorMessage = 'No se pudo cargar el perfil seleccionado.';
        this.isLoading = false;
        this.changeDetector.detectChanges();
      },
    });
  }

  onRedChange(redSocial: string): void {
    this.redSocial = redSocial;
    this.loadPerfil();
  }

  private renderCharts(): void {
    this.disposeCharts();

    if (this.timelineChartRef && this.interaccionesTiempo.length) {
      this.registerChart(
        this.timelineChartRef.nativeElement,
        this.timelineOption(),
      );
    }

    if (this.redChartRef && this.interaccionesPorRed.length) {
      this.registerChart(
        this.redChartRef.nativeElement,
        this.redOption(),
      );
    }

    if (this.detalleChartRef && this.detalleInteracciones.length) {
      this.registerChart(
        this.detalleChartRef.nativeElement,
        this.detalleOption(),
      );
    }
  }

  private registerChart(element: HTMLElement, option: EChartsCoreOption): void {
    const chart = createChart(element, option);
    const observer = observeChartResize(chart, element);
    this.charts.push(chart);
    this.resizeObservers.push(observer);
  }

  private disposeCharts(): void {
    this.resizeObservers.forEach((observer) => observer.disconnect());
    this.charts.forEach((chart) => chart.dispose());
    this.resizeObservers = [];
    this.charts = [];
  }

  private timelineOption(): EChartsCoreOption {
    return {
      color: ['#2563eb'],
      tooltip: { trigger: 'axis' },
      grid: { left: 44, right: 18, top: 28, bottom: 44 },
      xAxis: {
        type: 'category',
        boundaryGap: false,
        data: this.interaccionesTiempo.map((item) => item.fecha),
        axisLabel: { color: '#64748b' },
        axisLine: { lineStyle: { color: '#cbd5e1' } },
      },
      yAxis: {
        type: 'value',
        axisLabel: { color: '#64748b' },
        splitLine: { lineStyle: { color: '#e2e8f0' } },
      },
      series: [
        {
          type: 'line',
          smooth: true,
          symbolSize: 8,
          lineStyle: { width: 3 },
          areaStyle: { opacity: 0.12 },
          data: this.interaccionesTiempo.map((item) => item.interacciones),
        },
      ],
    };
  }

  private redOption(): EChartsCoreOption {
    return {
      tooltip: { trigger: 'axis' },
      grid: { left: 44, right: 16, top: 24, bottom: 42 },
      xAxis: {
        type: 'category',
        data: this.interaccionesPorRed.map((item) => item.red_social),
        axisLabel: { color: '#64748b' },
        axisLine: { lineStyle: { color: '#cbd5e1' } },
      },
      yAxis: {
        type: 'value',
        axisLabel: { color: '#64748b' },
        splitLine: { lineStyle: { color: '#e2e8f0' } },
      },
      series: [
        {
          type: 'bar',
          barMaxWidth: 48,
          itemStyle: { borderRadius: [6, 6, 0, 0] },
          data: this.interaccionesPorRed.map((item) => ({
            value: item.interacciones,
            itemStyle: { color: redSocialColor(item.red_social) },
          })),
        },
      ],
    };
  }

  private detalleOption(): EChartsCoreOption {
    return {
      color: [redSocialColor(this.redSocial)],
      tooltip: { trigger: 'axis' },
      grid: { left: 44, right: 16, top: 24, bottom: 56 },
      xAxis: {
        type: 'category',
        data: this.detalleInteracciones.map((item) => item.componente),
        axisLabel: { color: '#64748b', interval: 0, rotate: 22 },
        axisLine: { lineStyle: { color: '#cbd5e1' } },
      },
      yAxis: {
        type: 'value',
        axisLabel: { color: '#64748b' },
        splitLine: { lineStyle: { color: '#e2e8f0' } },
      },
      series: [
        {
          type: 'bar',
          barMaxWidth: 44,
          itemStyle: { borderRadius: [6, 6, 0, 0] },
          data: this.detalleInteracciones.map((item) => item.interacciones),
        },
      ],
    };
  }
}
