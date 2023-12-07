import { useEffect, useState } from 'react';
import './CardList.css';
import Pagination from '@mui/material/Pagination';
import Stack from '@mui/material/Stack';

import Card from '../Card/Card';

function CardList({items, matchedItems, onItemClick, onSearchMatch, itemToMatch, filteredItems}) {

  const [page, setPage] = useState(1);
  const [pages,setPages] = useState(Math.round(items.length/2));

  function handlePageChange(e, value) {
    setPage(value);
  }

  useEffect(() => {
    setPages((Math.round(filteredItems.length/5)))
  }, [filteredItems]) 

    return (
    <Stack spacing={2}>
      <ul className='cardlist'>
        {filteredItems.slice(5*(page-1), 5*page).map((item) => (
          <Card 
            item={item}
            key={item.product_key}
            matchedItems={matchedItems}
            onItemClick={onItemClick}
            onSearchMatch={onSearchMatch}
            itemToMatch={itemToMatch}
          />
        ))}
      </ul>
        <Pagination count={pages} shape="rounded" size="small" onChange={handlePageChange} />
    </Stack>
  );
}

export default CardList;
