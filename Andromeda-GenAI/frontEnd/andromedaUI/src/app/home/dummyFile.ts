import { Component } from '@angular/core';
import * as XLSX from 'xlsx';  // Import the xlsx library

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  jsonData: any[] = [];  // This will store the JSON data

  // Mapping of original column headers to custom keys
  columnMapping: { [key: string]: string } = {
    "Customer ID": "id",
    "Name": "customerName",
    "Age": "customerAge",
    "Email": "customerEmail"
  };

  constructor() {}

  // Function to handle file upload
  onFileChange(event: any): void {
    const file = event.target.files[0];  // Get the file from the input
    if (file) {
      this.readExcel(file);
    }
  }

  // Function to read and convert the Excel file to JSON
  readExcel(file: File): void {
    const reader = new FileReader();  // Create a FileReader instance

    reader.onload = (e: any) => {
      // Read the Excel file as binary string
      const binaryString = e.target.result;
      const workbook = XLSX.read(binaryString, { type: 'binary' });

      // Get the first sheet (You can customize this to use specific sheets)
      const worksheet = workbook.Sheets[workbook.SheetNames[0]];

      // Convert the worksheet to JSON where the keys are column headers
      this.jsonData = XLSX.utils.sheet_to_json(worksheet, { header: 1 });

      // Convert the array to the required format (key-value pair)
      this.jsonData = this.jsonData.slice(1).map((row: any) => {
        const rowData: any = {};
        
        // Map column headers to custom keys
        this.jsonData[0].forEach((header: string, index: number) => {
          const customKey = this.columnMapping[header] || header; // Use the mapping or the original header
          rowData[customKey] = row[index];
        });

        return rowData;
      });
    };

    reader.readAsBinaryString(file);  // Read the file as a binary string
  }
}
