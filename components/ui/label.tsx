import React from 'react';
import './label.css'; // Import the raw CSS file

export const Label = ({
  children,
  htmlFor,
  className = '',
  ...props
}: {
  children: React.ReactNode;
  htmlFor?: string;
  className?: string;
}) => {
  return (
    <label
      htmlFor={htmlFor}
      className={`label ${className}`} // Use the "label" class from the CSS file
      {...props}
    >
      {children}
    </label>
  );
};
