export const RED_SOCIAL_OPTIONS = [
  'Todas',
  'LinkedIn',
  'Instagram',
  'YouTube',
  'GitHub',
];
export const DEFAULT_RED_SOCIAL = RED_SOCIAL_OPTIONS[0];

const RED_SOCIAL_COLORS: Record<string, string> = {
  LinkedIn: '#0a66c2',
  Instagram: '#c13584',
  YouTube: '#ff0033',
  GitHub: '#24292f',
};

export function redSocialColor(redSocial: string): string {
  return RED_SOCIAL_COLORS[redSocial] ?? '#64748b';
}

export function maxValue<T>(items: T[], selector: (item: T) => number): number {
  return Math.max(1, ...items.map(selector));
}

export function percent(value: number, max: number): number {
  return Math.round((value / max) * 100);
}
