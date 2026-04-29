import { HttpClient, HttpParams } from '@angular/common/http';
import { inject, Injectable } from '@angular/core';
import { Observable } from 'rxjs';

import { GlobalResponse, PerfilResponse } from './models';

@Injectable({ providedIn: 'root' })
export class DashboardClientService {
  private readonly http = inject(HttpClient);
  private readonly baseUrl = 'http://127.0.0.1:8000/api';

  getEstudiantes(): Observable<string[]> {
    return this.http.get<string[]>(`${this.baseUrl}/estudiantes`);
  }

  getPerfil(estudiante: string, redSocial: string): Observable<PerfilResponse> {
    let params = new HttpParams().set('estudiante', estudiante);
    if (redSocial !== 'Todas') {
      params = params.set('red_social', redSocial);
    }

    return this.http.get<PerfilResponse>(`${this.baseUrl}/dashboard/perfil`, { params });
  }

  getGlobal(redSocial: string): Observable<GlobalResponse> {
    let params = new HttpParams();
    if (redSocial !== 'Todas') {
      params = params.set('red_social', redSocial);
    }

    return this.http.get<GlobalResponse>(`${this.baseUrl}/dashboard/global`, { params });
  }
}
