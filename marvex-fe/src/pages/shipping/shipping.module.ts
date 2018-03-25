import { NgModule } from '@angular/core';
import { IonicPageModule } from 'ionic-angular';
import { ShippingPage } from './shipping';
import { HttpClientModule, HttpClient } from '@angular/common/http';

@NgModule({
  declarations: [
    ShippingPage,
  ],
  imports: [
    IonicPageModule.forChild(ShippingPage),
    HttpClientModule,
  ],
})
export class ShippingPageModule {}
