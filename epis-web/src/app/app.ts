import { Component, inject } from '@angular/core';
import { Router, RouterLink, RouterLinkActive, RouterOutlet } from '@angular/router';

import { AuthClientService } from './core/auth-client.service';

@Component({
  selector: 'app-root',
  imports: [RouterLink, RouterLinkActive, RouterOutlet],
  templateUrl: './app.html',
  styleUrl: './app.scss'
})
export class App {
  protected readonly authService = inject(AuthClientService);
  protected readonly router = inject(Router);

  protected get isLoginRoute(): boolean {
    return this.router.url.startsWith('/login');
  }

  protected get isConsultedProfileRoute(): boolean {
    return this.router.url.startsWith('/estudiantes/');
  }

  logout(): void {
    this.authService.logout();
    this.router.navigateByUrl('/login');
  }
}
