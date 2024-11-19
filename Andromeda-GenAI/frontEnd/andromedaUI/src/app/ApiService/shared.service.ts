import { Injectable } from '@angular/core';
import { BehaviorSubject, Subject } from 'rxjs';
 
@Injectable({
  providedIn: 'root'  // Ensures that the service is a singleton throughout the app
})
export class SharedService {
  // Using BehaviorSubject to share data between components
  private listOfCustomers = new BehaviorSubject<any>(null);
 public  listOfCustomers$ = this.listOfCustomers.asObservable();
 
  constructor() { }
 
  // Method to update data
  nextCustomers(listOfCustomers: any): void {
    this.listOfCustomers.next(listOfCustomers);
  }
}