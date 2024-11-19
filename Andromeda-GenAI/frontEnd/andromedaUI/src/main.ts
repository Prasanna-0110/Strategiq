
import { platformBrowserDynamic } from '@angular/platform-browser-dynamic';  // Import platformBrowserDynamic to bootstrap Angular
import { AppModule } from './app/app.module';  // Import the AppModule (root module)

platformBrowserDynamic().bootstrapModule(AppModule)  // Bootstrap the AppModule


