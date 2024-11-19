// app-routing.module.ts
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';  // Import necessary modules
import { HomeComponent } from './home/home.component';  // Import HomeComponent
import { CustomerViewComponent } from './customer-view/customer-view.component';  // Import CustomerViewComponent
import { CustomerDetailViewComponent } from './customer-detail-view/customer-detail-view.component';

// Define routes as an array of objects
const routes: Routes = [
  { path: '', component: HomeComponent },  // Default route (Home page)
  { path: 'customer-view', component: CustomerViewComponent }, 
  {path: 'customer-detail-view', component: CustomerDetailViewComponent},// Route for customer view
  { path: '**', redirectTo: '' }  // Wildcard route (redirect to home for any unknown paths)
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],  // Configure routes in the RouterModule
  exports: [RouterModule]  // Export RouterModule to make it available throughout the app
})
export class AppRoutingModule {}
