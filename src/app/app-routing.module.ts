import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { MaterialModule } from './core/material/material.module';
import { LoginGuard } from './core/guards/login.guard';
import { AuthGuard } from './core/guards/auth.guard';

const routes: Routes = [
  {
    path: 'login',
    loadChildren: () =>
      import('./public/public.module').then((m) => m.PublicModule),
    canActivate: [LoginGuard],
  },
  {
    path: 'dashboard',
    loadChildren: () =>
      import('./private/private.module').then((m) => m.PrivateModule),
    // canActivate: [AuthGuard],
  },
  // redirect to public if no path is provided
  { path: '', redirectTo: 'login', pathMatch: 'full' },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
