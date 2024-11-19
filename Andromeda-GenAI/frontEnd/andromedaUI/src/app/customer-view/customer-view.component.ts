import { Component, OnInit, AfterViewInit, ElementRef, ViewChild, ViewEncapsulation } from '@angular/core';
import { Chart, ChartConfiguration, LinearScale, CategoryScale, BarElement, BarController, Title, Tooltip, Legend } from 'chart.js';
import { SharedService } from '../ApiService/shared.service';

// Registering the required components explicitly
Chart.register(LinearScale, CategoryScale, BarElement, BarController, Title, Tooltip, Legend);

@Component({
  selector: 'app-customer-view',
  templateUrl: './customer-view.component.html',
  styleUrls: ['./customer-view.component.scss'],
  encapsulation: ViewEncapsulation.None
})
export class CustomerViewComponent implements OnInit, AfterViewInit {
  @ViewChild('histogramCanvas') histogramCanvas!: ElementRef;
  public customers: any;
  public tableColumns: any = [];

  constructor(private sharedService: SharedService) {}

  ngOnInit(): void {
    this.sharedService.listOfCustomers$.subscribe((data: any) => {
      this.customers = data;
    
      console.log('column name', this.tableColumns);
    });
  }



  ngAfterViewInit(): void {
    this.loadCustomerData();
  }

  loadCustomerData(): void {
    const scoreCounts = this.calculateHistogramData(this.customers, 0.5);
    this.createHistogram(scoreCounts, 0.5);
  }

  calculateHistogramData(customers: any[], binSize: number): number[] {
    const scores = customers.map(customer => parseFloat(customer.cscore));
    const maxScore = 10;
    const binCount = Math.ceil(maxScore / binSize);
    const histogramData = new Array(binCount).fill(0);

    scores.forEach(score => {
      const binIndex = Math.floor(score / binSize);
      if (binIndex >= 0 && binIndex < binCount) {
        histogramData[binIndex]++;
      }
    });

    return histogramData.reverse(); // Reverse data for descending order
  }

  createHistogram(scoreCounts: number[], binSize: number): void {
    const canvas = this.histogramCanvas.nativeElement;

    const config: ChartConfiguration<'bar'> = {
      type: 'bar',
      data: {
        labels: scoreCounts.map((_, index) => (10 - index * binSize).toFixed(1)),
        datasets: [{
          label: 'Number of Customers',
          data: scoreCounts,
          backgroundColor: 'rgba(75, 192, 192, 0.5)',
          borderColor: 'rgba(75, 192, 192, 1)',
          borderWidth: 1,
          borderSkipped: false
        }]
      },
      options: {
        responsive: true,
        scales: {
          x: {
            type: 'linear',
            title: { display: true, text: 'Customer Score (cscore)' },
            min: 0, // End at 0
            max: 10,
            ticks: {
              stepSize: binSize,
              callback: value => `${parseFloat(value as string).toFixed(1)}`,
            },
            reverse: true // Reverse for descending order on display
          },
          y: {
            title: { display: true, text: 'Number of Customers' },
            beginAtZero: true,
            ticks: {
              stepSize: 1,
              callback: value => `${Math.floor(value as number)}`,
            }
          }
        }
      }
    };

    new Chart(canvas, config);
  }
}
