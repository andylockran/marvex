import { Component, Input } from '@angular/core';

/**
 * Generated class for the ShippingflagComponent component.
 *
 * See https://angular.io/api/core/Component for more info on Angular
 * Components.
 */
@Component({
  selector: 'shippingflag',
  templateUrl: 'shippingflag.html'
})
export class ShippingflagComponent {

  @Input() number: number;
  image: string = "";

  constructor() {
    console.log('Hello ShippingflagComponent Component');
    
  }

  ngOnChanges() {
    this.image = "/assets/shipflags/flag_" + this.number + ".png";
  }
}
