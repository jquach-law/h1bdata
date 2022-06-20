import Link from "next/link";
import React from "react";

export default function Navbar() {
  return (
    <nav class="navbar" role="navigation" aria-label="main navigation">
      <div class="navbar-brand">
        <Link href="/">
          <a class="navbar-item">H1B Data</a>
        </Link>
      </div>
    </nav>
  );
}
