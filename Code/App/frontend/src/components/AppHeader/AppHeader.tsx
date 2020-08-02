import React, { ReactElement } from 'react';
import './AppHeader.scss';

export function AppHeader(): ReactElement {
  return (
    <header className="app-header">
      <a
        className="app-header-link"
        href="https://sbercode.tech/"
        target="_blank"
        rel="noopener noreferrer"
      >
        Разработано в рамках хакатона "SBERCODE"
      </a>
      <a
        className="app-header-link"
      >
        АК
      </a>
    </header>
  );
}
