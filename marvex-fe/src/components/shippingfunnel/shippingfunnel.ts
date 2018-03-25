import { Component } from '@angular/core';

/**
 * Generated class for the ShippingfunnelComponent component.
 *
 * See https://angular.io/api/core/Component for more info on Angular
 * Components.
 */
@Component({
  selector: 'shippingfunnel',
  templateUrl: 'shippingfunnel.html'
})
export class ShippingfunnelComponent {

  text: string;

  constructor() {
    console.log('Hello ShippingfunnelComponent Component');
    this.text = 'Hello World';
  }

}
