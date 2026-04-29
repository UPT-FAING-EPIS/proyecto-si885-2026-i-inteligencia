import { Routes } from '@angular/router';

import { authGuard } from './core/auth.guard';
import { GlobalDashboardComponent } from './features/global-dashboard/global-dashboard';
import { LoginComponent } from './features/login/login';
import { PerfilDashboardComponent } from './features/perfil-dashboard/perfil-dashboard';

export const routes: Routes = [
  { path: 'login', component: LoginComponent },
  { path: 'perfil', component: PerfilDashboardComponent, canActivate: [authGuard] },
  { path: 'estudiantes/:estudiante', component: PerfilDashboardComponent, canActivate: [authGuard] },
  { path: 'global', component: GlobalDashboardComponent, canActivate: [authGuard] },
  { path: '', pathMatch: 'full', redirectTo: 'login' },
  { path: '**', redirectTo: 'login' },
];
