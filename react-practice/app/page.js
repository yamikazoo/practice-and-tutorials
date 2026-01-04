import LikeButton from './like-button';
 
function Header({ title }) {
  return <h1>{title ? title : 'Default title'}</h1>;
}

// export default sets this function as the main component of the page to be rendered
export default function HomePage() {
  const names = ['Ada Lovelace', 'Grace Hopper', 'Margaret Hamilton'];

  return (
    <div>
      <Header title="Develop. Six. Seven." />
      <ul>
        {names.map((name) => (
          <li key={name}>{name}</li>
        ))}
      </ul>
      <LikeButton />
    </div>
  );
}