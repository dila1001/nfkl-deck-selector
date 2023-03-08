import { ChangeDetectionStrategy, Component, OnInit } from '@angular/core';
import { NavItem } from '../../models/navbar.model';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class NavbarComponent implements OnInit {
  navItems: NavItem[] = [
    { name: 'Decks', url: '' },
    { name: 'Games', url: '' },
    { name: 'Profile', url: '' },
    { name: 'Divisions', url: '' },
    { name: 'Statistics', url: '', children: [] },
    { name: 'Admin', url: '' },
  ];

  constructor() {}

  ngOnInit(): void {}
}
