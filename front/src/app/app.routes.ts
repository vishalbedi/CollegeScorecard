import { Routes } from '@angular/router';
import { HomeComponent } from './home';
import { AboutComponent } from './about';
import { NoContentComponent } from './no-content';

import { LoginFormComponent } from './login';
import { NotFoundComponent } from './utils';
import { DataResolver } from './app.resolver';

export const ROUTES: Routes = [
  {
    path: '',
    redirectTo: '/home',
    pathMatch: 'full'
  },
  { path: 'home', component: HomeComponent },
  { path: '**', component: NotFoundComponent }
];
