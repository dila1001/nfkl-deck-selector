import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root',
})
export class AuthService {
  private readonly ACCESS_TOKEN = 'token';
  private readonly REFRESH_TOKEN = 'refresh_token';
  private path = environment.apiUrl;

  constructor(private http: HttpClient) {}

  public signOutExternal = () => {
    localStorage.removeItem(this.ACCESS_TOKEN);
    console.log('token deleted');
  };

  loginWithGoogle(credentials: string): Observable<any> {
    const header = new HttpHeaders().set('Content-type', 'application/json');
    return this.http.post(
      this.path + 'loginWithGoogle',
      JSON.stringify(credentials),
      { headers: header }
    );
  }

  isLoggedIn(): boolean {
    return !!this.getAccessToken();
  }

  getAccessToken(): string | null {
    return (
      localStorage.getItem(this.ACCESS_TOKEN) ||
      sessionStorage.getItem(this.ACCESS_TOKEN)
    );
  }
}
