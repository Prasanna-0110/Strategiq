import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable , of} from 'rxjs';

import data from './customerViewMock.json'

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private apiUrl = 'http://localhost:8000/api/items/create/'; // Replace with your actual API URL

  constructor(private http: HttpClient) {}

  uploadFile(requestBody: any): Observable<any> {
    // Prepare form data
    //const formData = new FormData();
    //formData.append('file', file);

    // Set headers if needed (optional)
    //const headers = new HttpHeaders();

    const headers = new HttpHeaders({
      'Content-Type': 'application/json'  // Set the Content-Type header to application/json
    });
console.log('Request body', requestBody);
    // Send POST request to upload file
    return this.http.post<any>(this.apiUrl, requestBody, { headers });

   // return of(data);
  }
}
