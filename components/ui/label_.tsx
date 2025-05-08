
export function Label({ htmlFor, children }) {
  return <label htmlFor={htmlFor} className="block font-semibold mb-1">{children}</label>;
}
