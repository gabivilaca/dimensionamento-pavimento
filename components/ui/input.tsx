import React from 'react';
import './input.css'; // Import the raw CSS file

export const Input = React.forwardRef<HTMLInputElement, React.InputHTMLAttributes<HTMLInputElement>>(
  ({ className = '', ...props }, ref) => (
    <input
      ref={ref}
      className={`input ${className}`} // Use the "input" class from the CSS file
      {...props}
    />
  )
);
Input.displayName = 'Input';
