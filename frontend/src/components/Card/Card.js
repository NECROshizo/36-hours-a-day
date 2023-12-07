import './Card.css';
import {Link} from 'react-router-dom';

function Card({item, isMatched, onItemClick, onSearchMatch}) {


  function handleFindMatched(item) {
    return onSearchMatch(item)
  }

  function handleOpenItem() {
    onItemClick(item);
  }

  return (
    <li className='card'>
      <Link className='card__link' to={`${item.id}`} onClick={handleOpenItem}>
        <h1 className='card__title'>{item.product_name}</h1>
      </Link>
        <div className={isMatched ? 'card__status card__status_type_done' : 'card__status'}></div>
        <p className='card__date'>{item.date}</p>
        <p className='card__price'>{item.price}</p>
        <p className='card__prod-name'>{handleFindMatched(item)}</p>
    </li>
      
  );
}

export default Card;
