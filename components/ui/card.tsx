import React from 'react';
import './card.css';

export const Card = ({ children, className = '', ...props }: { children: React.ReactNode; className?: string }) => {
  return (
    <div className={`card ${className}`} {...props}>
      {children}
    </div>
  );
};

export function CardContent({ children }: { children: React.ReactNode }) {
  return <div className="card-content">{children}</div>;
}
