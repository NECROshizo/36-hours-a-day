import './Card.css';
import {Link} from 'react-router-dom';
import { useEffect, useState } from 'react';

function Card({item, onItemClick}) {

  const [isMatched, setIsMatched] = useState(false);

  function handleOpenItem() {
    onItemClick(item);
  }

  useEffect(() => {
    setIsMatched(item.is_defined);
  }, [])

  return (
    <li className='card'>
      <Link className='card__link' to={`${item.id}`} onClick={handleOpenItem}>
        <h1 className='card__title'>{item.product_name}</h1>
      </Link>
        <div className={isMatched ? 'card__status card__status_type_done' : 'card__status'}></div>
        <p className='card__date'>{item.date}</p>
        <p className='card__price'>{item.price}</p>
        <p className='card__prod-name'>{isMatched ? item.product_cust.name : ''}</p>
    </li>
      
  );
}

export default Card;
