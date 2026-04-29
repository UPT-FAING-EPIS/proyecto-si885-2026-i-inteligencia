import { BarChart, LineChart, PieChart } from 'echarts/charts';
import {
  GridComponent,
  LegendComponent,
  TooltipComponent,
} from 'echarts/components';
import { init, use, type ECharts, type EChartsCoreOption } from 'echarts/core';
import { CanvasRenderer } from 'echarts/renderers';

use([
  BarChart,
  CanvasRenderer,
  GridComponent,
  LegendComponent,
  LineChart,
  PieChart,
  TooltipComponent,
]);

export function createChart(element: HTMLElement, option: EChartsCoreOption): ECharts {
  const chart = init(element);
  chart.setOption(option, true);
  return chart;
}

export function observeChartResize(chart: ECharts, element: HTMLElement): ResizeObserver {
  const observer = new ResizeObserver(() => chart.resize());
  observer.observe(element);
  return observer;
}
