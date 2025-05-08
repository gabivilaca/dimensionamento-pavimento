
export function Button({ children, ...props }) {
  return (
    <button {...props} className="bg-blue-600 text-white p-2 rounded w-full hover:bg-blue-700">
      {children}
    </button>
  );
}
