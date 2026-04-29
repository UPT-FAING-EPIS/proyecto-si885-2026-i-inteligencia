import { HttpClient } from '@angular/common/http';
import { inject, Injectable } from '@angular/core';
import { map, Observable, tap } from 'rxjs';

import { ApiSessionResponse, SessionModel } from './models';

@Injectable({ providedIn: 'root' })
export class AuthClientService {
  private readonly http = inject(HttpClient);
  private readonly baseUrl = 'http://127.0.0.1:8000/api/auth';
  private readonly sessionKey = 'epis.session';

  login(username: string, password: string): Observable<SessionModel> {
    return this.http
      .post<ApiSessionResponse>(`${this.baseUrl}/login`, { username, password })
      .pipe(
        map((response) => ({
          estudiante: response.estudiante,
          displayName: response.display_name,
          username: response.username,
          accessToken: response.access_token,
          tokenType: response.token_type,
          isAuthenticated: response.is_authenticated,
        })),
        tap((session) => sessionStorage.setItem(this.sessionKey, JSON.stringify(session))),
      );
  }

  logout(): void {
    sessionStorage.removeItem(this.sessionKey);
  }

  getSession(): SessionModel | null {
    const rawSession = sessionStorage.getItem(this.sessionKey);
    return rawSession ? (JSON.parse(rawSession) as SessionModel) : null;
  }

  isAuthenticated(): boolean {
    const session = this.getSession();
    return session?.isAuthenticated === true && !!session.accessToken;
  }

  getAccessToken(): string | null {
    return this.getSession()?.accessToken ?? null;
  }
}
