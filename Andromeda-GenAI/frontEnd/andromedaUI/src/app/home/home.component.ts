import { Component, ViewEncapsulation } from '@angular/core';
import { ApiService } from '../ApiService/api.service';
import { Router } from '@angular/router';
import { SharedService } from '../ApiService/shared.service';
import * as XLSX from 'xlsx';  // Import xlsx library




@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss'],
  encapsulation: ViewEncapsulation.None
})
export class HomeComponent {
  selectedFile: File | null = null;
  jsonData: any[] = [];  // This will store the JSON data

  columnMapping: { [key: string]: string } = {
    "Customer ID": "customerId",
    "Name": "customerName",
    "Age": "age",
    "Gender": "gender",
     "Marital Status": "maritalStatus",
     "Income (Annual)": "income",
     "Occupation": "occupation",
     "Credit Score": "creditScore",
     "Outstanding Loans" : "outStandingLoans",
     "Banking History": "bankingHistory",
     "Current Account Balance": "currentAccountBalance",
     "Savings Account Balance": "savingsAccountBalance",
     "Mortgage/Property Ownership": "propertyOwnership",
     "Vehicle Owned": "vehicleOwned",
     "Insurance Coverage": "insuranceCoverage",
     "Investment Portfolio": "invetsmentPOrtfolio",
     "Digital Banking Usage": "digitalBankingUsage",
     "Risk Appetite": "riskAppetite",
     "Location": "location",
     "Spending Habits": "spendingHabits"
  };
  


  constructor(private apiService: ApiService, private router: Router, private sharedService: SharedService) {}

  onFileSelected(event: Event) {
    const input = event.target as HTMLInputElement;
    if (input.files && input.files.length > 0) {
      this.selectedFile = input.files[0];
      if (this.selectedFile) {
        this.readExcel(this.selectedFile);
      }
      console.log('File selected:', this.selectedFile.name);
    }
  }


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
      console.log('JSON data', this.jsonData);
    };

    reader.readAsBinaryString(file);  // Read the file as a binary string
  }

  uploadFile() {
    if (this.jsonData) {
     
     const data = this.jsonData;

     const req = {
       customers: data
     };

      this.apiService.uploadFile(req).subscribe(
        (response: any) => {
          console.log('File uploaded successfully', response);
          this.sharedService.nextCustomers(response.customers);
          // Navigate to the Customer View component with the response data
          this.router.navigate(['/customer-view']);
        },
        (error: any) => {
          console.log('Error uploading file', error);
        }
      );
    } else {
      alert('Please select a file first!');
    }
  }
}
