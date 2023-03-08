import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { PublicRoutingModule } from './public-routing.module';
import { PublicComponent } from './public.component';
import { LoginComponent } from './components/login/login.component';
import { MaterialModule } from '../core/material/material.module';
import { FormsModule } from '@angular/forms';
import { SharedModule } from '../shared/shared.module';

@NgModule({
  declarations: [PublicComponent, LoginComponent],
  imports: [CommonModule, PublicRoutingModule, MaterialModule, SharedModule],
})
export class PublicModule {}
