import React from 'react';
import './button.css'; // Import the raw CSS file

export const Button = ({
  children,
  onClick,
  className = '',
  ...props
}: {
  children: React.ReactNode;
  onClick?: () => void;
  className?: string;
}) => {
  return (
    <button
      onClick={onClick}
      className={`button ${className}`} // Use the "button" class from the CSS file
      {...props}
    >
      {children}
    </button>
  );
};
