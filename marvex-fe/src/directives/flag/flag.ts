import { Directive } from '@angular/core';

/**
 * Generated class for the FlagDirective directive.
 *
 * See https://angular.io/api/core/Directive for more info on Angular
 * Directives.
 */
@Directive({
  selector: '[flag]' // Attribute selector
})
export class FlagDirective {

  constructor() {
    console.log('Hello FlagDirective Directive');
  }

}
