import { DecimalPipe } from '@angular/common';
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
import { Router } from '@angular/router';
import type { ECharts, EChartsCoreOption } from 'echarts/core';

import { DashboardClientService } from '../../core/dashboard-client.service';
import {
  AlcancePorCicloModel,
  ContextoRedModel,
  DetalleInteraccionesModel,
  InteraccionesPorRedModel,
  TopEngagementModel,
} from '../../core/models';
import { createChart, observeChartResize } from '../../shared/echarts-utils';
import {
  DEFAULT_RED_SOCIAL,
  RED_SOCIAL_OPTIONS,
  redSocialColor,
} from '../../shared/dashboard-utils';

@Component({
  selector: 'app-global-dashboard',
  imports: [DecimalPipe, FormsModule],
  templateUrl: './global-dashboard.html',
  styleUrl: './global-dashboard.scss',
})
export class GlobalDashboardComponent implements OnInit, OnDestroy {
  @ViewChild('alcanceChart') private alcanceChartRef?: ElementRef<HTMLDivElement>;
  @ViewChild('redPieChart') private redPieChartRef?: ElementRef<HTMLDivElement>;
  @ViewChild('detalleChart') private detalleChartRef?: ElementRef<HTMLDivElement>;

  readonly redOptions = RED_SOCIAL_OPTIONS;
  redSocial = DEFAULT_RED_SOCIAL;
  alcancePorCiclo: AlcancePorCicloModel[] = [];
  contextoRed: ContextoRedModel | null = null;
  detalleInteracciones: DetalleInteraccionesModel[] = [];
  estudiantes: string[] = [];
  interaccionesPorRed: InteraccionesPorRedModel[] = [];
  searchEstudiante = '';
  searchMessage = '';
  topEngagement: TopEngagementModel[] = [];
  isLoading = false;
  errorMessage = '';

  private readonly changeDetector = inject(ChangeDetectorRef);
  private readonly dashboardService = inject(DashboardClientService);
  private readonly router = inject(Router);
  private charts: ECharts[] = [];
  private resizeObservers: ResizeObserver[] = [];

  ngOnInit(): void {
    this.loadEstudiantes();
    this.loadGlobal();
  }

  ngOnDestroy(): void {
    this.disposeCharts();
  }

  get estudiantesFiltrados(): string[] {
    const term = this.searchEstudiante.trim().toLowerCase();
    if (!term) {
      return this.estudiantes.slice(0, 8);
    }

    return this.estudiantes
      .filter((estudiante) => estudiante.toLowerCase().includes(term))
      .slice(0, 8);
  }

  loadGlobal(): void {
    this.disposeCharts();
    this.isLoading = true;
    this.errorMessage = '';
    this.changeDetector.detectChanges();

    this.dashboardService.getGlobal(this.redSocial).subscribe({
      next: (response) => {
        this.alcancePorCiclo = response.alcance_por_ciclo;
        this.contextoRed = response.contexto_red;
        this.detalleInteracciones = response.detalle_interacciones;
        this.interaccionesPorRed = response.interacciones_por_red;
        this.topEngagement = response.top_engagement;
        this.isLoading = false;
        this.changeDetector.detectChanges();
        setTimeout(() => this.renderCharts());
      },
      error: () => {
        this.errorMessage = 'No se pudo cargar el impacto global.';
        this.isLoading = false;
        this.changeDetector.detectChanges();
      },
    });
  }

  onRedChange(redSocial: string): void {
    this.redSocial = redSocial;
    this.loadGlobal();
  }

  openPerfil(estudiante: string): void {
    const selected = this.findEstudiante(estudiante);
    if (!selected) {
      this.searchMessage = 'Selecciona un estudiante válido de la lista.';
      this.changeDetector.detectChanges();
      return;
    }

    this.searchMessage = '';
    this.router.navigate(['/estudiantes', selected]);
  }

  private loadEstudiantes(): void {
    this.dashboardService.getEstudiantes().subscribe({
      next: (estudiantes) => {
        this.estudiantes = estudiantes;
        this.changeDetector.detectChanges();
      },
      error: () => {
        this.searchMessage = 'No se pudo cargar la lista de estudiantes.';
        this.changeDetector.detectChanges();
      },
    });
  }

  private findEstudiante(estudiante: string): string | null {
    const normalized = estudiante.trim().toLowerCase();
    return (
      this.estudiantes.find((item) => item.toLowerCase() === normalized) ??
      this.estudiantes.find((item) => item.toLowerCase().includes(normalized)) ??
      null
    );
  }

  private renderCharts(): void {
    this.disposeCharts();

    if (this.alcanceChartRef && this.alcancePorCiclo.length) {
      this.registerChart(
        this.alcanceChartRef.nativeElement,
        this.alcanceOption(),
      );
    }

    if (this.redPieChartRef && this.interaccionesPorRed.length) {
      this.registerChart(
        this.redPieChartRef.nativeElement,
        this.redPieOption(),
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

  private alcanceOption(): EChartsCoreOption {
    return {
      color: ['#2563eb'],
      tooltip: { trigger: 'axis' },
      grid: { left: 52, right: 18, top: 28, bottom: 42 },
      xAxis: {
        type: 'category',
        data: this.alcancePorCiclo.map((item) => item.ciclo),
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
          barMaxWidth: 42,
          itemStyle: { borderRadius: [6, 6, 0, 0] },
          data: this.alcancePorCiclo.map((item) => item.alcance),
        },
      ],
    };
  }

  private redPieOption(): EChartsCoreOption {
    return {
      tooltip: { trigger: 'item' },
      legend: {
        bottom: 0,
        textStyle: { color: '#475569' },
      },
      series: [
        {
          type: 'pie',
          radius: ['48%', '72%'],
          center: ['50%', '43%'],
          avoidLabelOverlap: true,
          label: {
            color: '#334155',
            formatter: '{b}\n{d}%',
          },
          data: this.interaccionesPorRed.map((item) => ({
            name: item.red_social,
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
