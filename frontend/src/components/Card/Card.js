import './Card.css';
import {Link} from 'react-router-dom';
import { useEffect, useState } from 'react';

function Card({item, onItemClick, onSearchMatch}) {

  const [isMatched, setIsMatched] = useState(false);

  function handleFindMatched(item) {
    return onSearchMatch(item)
  }

  function handleOpenItem() {
    onItemClick(item);
  }

  useEffect(() => {
    console.log(item);
  }, [])

  return (
    <li className='card'>
      <Link className='card__link' to={`${item.id}`} onClick={handleOpenItem}>
        <h1 className='card__title'>{item.product_name}</h1>
      </Link>
        <div className={isMatched ? 'card__status card__status_type_done' : 'card__status'}></div>
        <p className='card__date'>{item.date}</p>
        <p className='card__price'>{item.price}</p>
        <p className='card__prod-name'>{isMatched ? handleFindMatched(item) : ''}</p>
    </li>
      
  );
}

export default Card;
