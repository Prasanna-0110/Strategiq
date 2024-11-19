import { Component, OnInit, AfterViewInit, ViewChild, ElementRef, OnDestroy } from '@angular/core';
import { Chart, registerables } from 'chart.js';

// Register all necessary chart components
Chart.register(...registerables);

@Component({
  selector: 'app-customer-detail-view',
  templateUrl: './customer-detail-view.component.html',
  styleUrls: ['./customer-detail-view.component.scss']
})
export class CustomerDetailViewComponent implements OnInit, AfterViewInit, OnDestroy {
  customerDetails: { key: string, value: any }[] = [];
  isCollapsed: boolean = false; // Single collapse state for "Show Customer Data"

  customerData =          {
    "customerId": "1004",
    "age": "54",
    "gender": "M",
    "maritalStatus": "Divorced",
    "income": "150000",
    "occupation": "Doctor",
    "creditScore": "800",
    "outStandingLoans": "20000",
    "bankingHistory": "Savings--Home Loan--Credit Card",
    "currentAccountBalance": "20000",
    "savingsAccountBalance": "30000",
    "propertyOwnership": "Yes",
    "vehicleOwned": "Yes",
    "insuranceCoverage": "Health--Life--Home",
    "investmentPortfolio": "Stocks--Bonds",
    "digitalBankingUsage": "High",
    "riskAppetite": "Moderate",
    "location": "San Francisco",
    "spendingHabits": "High",
    "cscore": "8",
    "services": [
        {
            "serviceName": "Savings Account",
            "sscore": "9",
            "pitchDesciption": "With your current savings account balance and steady income, a high-yield savings account can help you maximize your savings. It offers competitive interest rates and easy access to your funds. By keeping your money in a high-yield savings account, you can watch your balance grow over time while maintaining financial flexibility."
        },
        {
            "serviceName": "Current Account",
            "sscore": "8",
            "pitchDesciption": "A current account is essential for managing your day-to-day financial transactions. With features like overdraft protection and easy access to funds, it provides convenience and financial security. Given your high digital banking usage, a current account with comprehensive online and mobile banking services will ensure you can manage your finances seamlessly."
        },
        {
            "serviceName": "Fixed Deposits",
            "sscore": "7",
            "pitchDesciption": "Fixed deposits are a safe and reliable way to earn higher interest rates on your savings. By locking in your funds for a set period, you can benefit from guaranteed returns. This is an excellent option for you, given your moderate risk appetite and desire for stable investments."
        },
        {
            "serviceName": "Personal Loan",
            "sscore": "5",
            "pitchDesciption": "A personal loan can provide quick access to funds for various needs, such as medical expenses or home renovations. With your excellent credit score, you can benefit from lower interest rates and flexible repayment terms. This is a convenient option if you need additional funds without tapping into your savings."
        },
        {
            "serviceName": "Home Loan",
            "sscore": "4",
            "pitchDesciption": "Given that you already own a property, a home loan may not be a priority for you at this moment. However, if you are considering purchasing another property or refinancing, our competitive home loan rates and flexible terms can help you achieve your goals with ease."
        },
        {
            "serviceName": "Educational Loan",
            "sscore": "3",
            "pitchDesciption": "An educational loan is a great option for funding higher education. While this may not be relevant to you personally, it could be beneficial if you are considering financing education for your children or dependents. We offer competitive rates and flexible repayment options to support your educational aspirations."
        },
        {
            "serviceName": "Vehicle Loan",
            "sscore": "4",
            "pitchDesciption": "As you already own a vehicle, a vehicle loan might not be your immediate requirement. However, if you are planning to upgrade or purchase another vehicle, our vehicle loans offer attractive interest rates and flexible repayment options to make your purchase more affordable."
        },
        {
            "serviceName": "Cheque Payments",
            "sscore": "5",
            "pitchDesciption": "Cheque payments are a secure and traditional way to manage transactions. While digital banking is more convenient, having the option to use cheques can be beneficial for certain payments and transactions. It provides an additional layer of financial flexibility."
        },
        {
            "serviceName": "Credit Card",
            "sscore": "9",
            "pitchDesciption": "A credit card is an essential tool for managing your expenses and earning rewards. With your excellent credit score, you can qualify for premium credit cards that offer higher credit limits, cashback, travel rewards, and other exclusive benefits. This will enhance your spending power and provide additional financial security."
        },
        {
            "serviceName": "Online and Mobile Banking",
            "sscore": "10",
            "pitchDesciption": "Given your high digital banking usage, online and mobile banking services are crucial for managing your finances. Our comprehensive digital banking platform offers features like real-time transaction alerts, easy fund transfers, and bill payments. It ensures you have complete control over your finances anytime, anywhere."
        },
        {
            "serviceName": "Foreign Exchange",
            "sscore": "6",
            "pitchDesciption": "If you travel frequently or engage in international transactions, our foreign exchange services can provide you with competitive rates and convenient currency exchange options. This will help you manage your international finances more efficiently."
        },
        {
            "serviceName": "Investment Services",
            "sscore": "8",
            "pitchDesciption": "With your existing investment portfolio, our investment services can help you diversify and optimize your investments. We offer personalized investment advice, portfolio management, and access to a wide range of investment options to help you achieve your financial goals."
        },
        {
            "serviceName": "Life Insurance",
            "sscore": "7",
            "pitchDesciption": "Life insurance is an essential component of your financial plan, providing financial security for your loved ones. With your existing coverage, you can consider additional policies to enhance your protection. Our life insurance plans offer flexible terms and competitive premiums to suit your needs."
        },
        {
            "serviceName": "Health Insurance",
            "sscore": "8",
            "pitchDesciption": "Health insurance is crucial for managing medical expenses and ensuring access to quality healthcare. With your current coverage, you can explore additional policies or higher coverage limits to enhance your protection. Our health insurance plans offer comprehensive coverage and flexible options to meet your healthcare needs."
        },
        {
            "serviceName": "Property Insurance",
            "sscore": "7",
            "pitchDesciption": "Property insurance is vital for protecting your valuable assets. With your existing coverage, you can consider additional policies or higher coverage limits to ensure comprehensive protection for your property. Our property insurance plans offer flexible terms and competitive premiums to suit your needs."
        },
        {
            "serviceName": "Wealth Management",
            "sscore": "9",
            "pitchDesciption": "Wealth management services are designed to help you grow and protect your wealth. Our personalized wealth management solutions include investment advice, portfolio management, and financial planning. Given your high income and investment portfolio, our wealth management services can help you achieve your financial goals and secure your financial future."
        },
        {
            "serviceName": "Safe Deposit Boxes",
            "sscore": "6",
            "pitchDesciption": "Safe deposit boxes provide a secure place to store your valuable documents and possessions. Given your property ownership and investment portfolio, having a safe deposit box can offer peace of mind and additional security for your important assets."
        }
    ]
}


  @ViewChild('chartRef') chartRef!: ElementRef<HTMLCanvasElement>; // Canvas reference for Chart.js
  chart: any;

  ngOnInit(): void {
    this.prepareCustomerDetails();


  }

  // Prepare the customer details data for display
  prepareCustomerDetails(): void {
    for (let key in this.customerData) {
      if (key !== 'services') {
        this.customerDetails.push({ key, value: this.customerData[key as keyof typeof this.customerData] });
      }
    }
  }

  // Ensure the chart is initialized after the view is fully initialized
  ngAfterViewInit(): void {
    console.log('ngAfterViewInit triggered');
    this.initChart();
  
    
  }

  toggleCollapse(): void {
    this.isCollapsed = !this.isCollapsed; // Toggle the collapse state for the "Show Customer Data" section
  }

  // Initialize Chart.js for histogram
  initChart(): void {
    console.log('Initializing chart...');

    // Ensure the canvas reference is available
    const canvas = this.chartRef.nativeElement;
    if (!canvas) {
      console.error('Chart canvas not found!');
      return;
    }

    console.log('Canvas found, proceeding to create chart');

    // Initialize the chart only if the canvas is available
    this.chart = new Chart(canvas, {
      type: 'bar', // Bar chart type
      data: {
        labels: this.customerData.services.map(service => service.serviceName), // X-axis: Service Names
        datasets: [{
          label: 'Score',
          data: this.customerData.services.map(service => parseInt(service.sscore)), // Y-axis: Service Scores
          backgroundColor: 'rgba(0, 123, 255, 0.5)', // Bar color
          borderColor: 'rgba(0, 123, 255, 1)', // Border color
          borderWidth: 1
        }]
      },
      options: {
        responsive: true,
        scales: {
          x: {
            title: {
              display: true,
              text: 'Service Name'
            }
          },
          y: {
            title: {
              display: true,
              text: 'Score'
            },
            min: 0, // Set minimum score to 0
            ticks: {
              stepSize: 1 // Control the interval between ticks on the Y-axis
            }
          }
        }
      }
    });
    console.log('Chart initialized');
  }

  // Clean up chart when component is destroyed
  ngOnDestroy(): void {
    if (this.chart) {
      this.chart.destroy();
    }
  }
}
