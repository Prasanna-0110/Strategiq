import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { ApiService } from './ApiService/api.service'; // import ApiService here
import { SharedService } from './ApiService/shared.service';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { HttpClientModule } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import {AppComponent} from './app.component';
import {HomeComponent} from './home/home.component';
import { CustomerViewComponent } from './customer-view/customer-view.component';  // Import CustomerViewComponent
import { CommonModule } from '@angular/common';
import { CustomerDetailViewComponent } from './customer-detail-view/customer-detail-view.component';
import { NgbCollapseModule } from '@ng-bootstrap/ng-bootstrap';


@NgModule({
  declarations: [
 AppComponent,
    HomeComponent,  // Declare HomeComponent
    CustomerViewComponent,
    CustomerDetailViewComponent
    // your other components
  ],
  imports: [
    BrowserModule,
    CommonModule,
    NgbCollapseModule,
    HttpClientModule,
    AppRoutingModule

    // other imports
  ],
  providers: [ApiService, SharedService],
  bootstrap: [AppComponent]
})
export class AppModule {}
