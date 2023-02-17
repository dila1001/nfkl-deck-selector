import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class AuthService {
  private readonly ACCESS_TOKEN = 'ACCESS_TOKEN';
  private readonly REFRESH_TOKEN = 'REFRESH_TOKEN';

  constructor() {}

  isLoggedIn() {
    return !!this.getAccessToken();
  }

  getAccessToken() {
    return (
      localStorage.getItem(this.ACCESS_TOKEN) ||
      sessionStorage.getItem(this.ACCESS_TOKEN)
    );
  }
}
