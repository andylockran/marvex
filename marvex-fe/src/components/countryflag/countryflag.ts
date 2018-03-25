import { Component, Input } from '@angular/core';

/**
 * Generated class for the CountryflagComponent component.
 *
 * See https://angular.io/api/core/Component for more info on Angular
 * Components.
 */
@Component({
  selector: 'countryflag',
  templateUrl: 'countryflag.html'
})
export class CountryflagComponent {

  @Input() country: string;

  ionViewDidLoad() {
    console.log('Loaded ', this.country);
  }

}
