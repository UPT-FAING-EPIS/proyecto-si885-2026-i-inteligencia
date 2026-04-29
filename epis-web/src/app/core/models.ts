export type RedSocial = 'LinkedIn' | 'Instagram' | 'YouTube' | 'GitHub';

export interface SessionModel {
  estudiante: string;
  displayName: string;
  username: string;
  accessToken: string;
  tokenType: string;
  isAuthenticated: boolean;
}

export interface ApiSessionResponse {
  estudiante: string;
  display_name: string;
  username: string;
  access_token: string;
  token_type: string;
  is_authenticated: boolean;
}

export interface PerfilMetricasModel {
  total_publicaciones: number;
  total_interacciones: number;
  red_favorita: string;
}

export interface InteraccionesTiempoModel {
  fecha: string;
  interacciones: number;
}

export interface InteraccionesPorRedModel {
  red_social: string;
  interacciones: number;
}

export interface DetalleInteraccionesModel {
  componente: string;
  interacciones: number;
}

export interface AlcancePorCicloModel {
  ciclo: string;
  alcance: number;
}

export interface TopEngagementModel {
  estudiante: string;
  publicaciones: number;
  alcance: number;
  interacciones: number;
  engagement_rate: number;
}

export interface ContextoRedModel {
  red_social: string;
  tipo_alcance: string;
  tipo_interaccion: string;
  componentes: string[];
}

export interface PerfilResponse {
  metricas: PerfilMetricasModel;
  interacciones_tiempo: InteraccionesTiempoModel[];
  interacciones_por_red: InteraccionesPorRedModel[];
  detalle_interacciones: DetalleInteraccionesModel[];
  contexto_red: ContextoRedModel;
}

export interface GlobalResponse {
  alcance_por_ciclo: AlcancePorCicloModel[];
  interacciones_por_red: InteraccionesPorRedModel[];
  detalle_interacciones: DetalleInteraccionesModel[];
  top_engagement: TopEngagementModel[];
  contexto_red: ContextoRedModel;
}
