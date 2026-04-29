import { Component, inject, OnInit } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { Router } from '@angular/router';

import { AuthClientService } from '../../core/auth-client.service';

@Component({
  selector: 'app-login',
  imports: [FormsModule],
  templateUrl: './login.html',
  styleUrl: './login.scss',
})
export class LoginComponent implements OnInit {
  username = '';
  password = 'epis123';
  errorMessage = '';

  private readonly authService = inject(AuthClientService);
  private readonly router = inject(Router);

  ngOnInit(): void {
    if (this.authService.isAuthenticated()) {
      this.router.navigateByUrl('/perfil');
      return;
    }
  }

  submitLogin(): void {
    const username = this.username.trim();

    if (!username || !this.password) {
      return;
    }

    this.errorMessage = '';
    this.authService.login(username, this.password).subscribe({
      next: () => this.router.navigateByUrl('/perfil'),
      error: () => {
        this.errorMessage =
          'C\u00f3digo universitario o contrase\u00f1a incorrectos.';
      },
    });
  }
}
