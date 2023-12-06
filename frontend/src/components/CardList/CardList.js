import { useEffect, useState } from 'react';
import './CardList.css';
import Pagination from '@mui/material/Pagination';
import Stack from '@mui/material/Stack';

import Card from '../Card/Card';

function CardList({items, matchedItems, onItemClick, onSearchMatch, statusFilter, itemToMatch, checkIsMatched, onFilterChange, filteredItems}) {

  const [page, setPage] = useState(1);
  const [pages, setPages] = useState(Math.round(filteredItems.length/2))

  function handlePageChange(e, value) {
    setPage(value);
  }

  useEffect(() => {
    setPages(Math.round(filteredItems.length/2))
  }, [filteredItems]) 

    return (
    <Stack spacing={2}>
      {((statusFilter === 'all') || (statusFilter === '')) && <ul className='cardlist'>
        {filteredItems.slice(2*(page-1), 2*page).map((item) => (
          <Card 
            item={item}
            key={item.id}
            isMatched={checkIsMatched(matchedItems, item)}
            matchedItems={matchedItems}
            onItemClick={onItemClick}
            onSearchMatch={onSearchMatch}
            itemToMatch={itemToMatch}
          />
        ))}
      </ul>}
      {(statusFilter === 'yes') && <ul className='cardlist'>
        {filteredItems.slice(2*(page-1), 2*page).map((item) => (
          <Card 
            item={item}
            key={item.id}
            isMatched={checkIsMatched(matchedItems, item)}
            matchedItems={matchedItems}
            onItemClick={onItemClick}
            onSearchMatch={onSearchMatch}
            itemToMatch={itemToMatch}
          />
        ))}
      </ul>}
      {(statusFilter === 'no') && <ul className='cardlist'>
        {filteredItems.slice(2*(page-1), 2*page).map((item) => (
          <Card 
            item={item}
            key={item.id}
            isMatched={checkIsMatched(matchedItems, item)}
            matchedItems={matchedItems}
            onItemClick={onItemClick}
            onSearchMatch={onSearchMatch}
            itemToMatch={itemToMatch}
          />
        ))}
      </ul>}
        <Pagination count={pages} shape="rounded" size="small" onChange={handlePageChange} />
    </Stack>
  );
}

export default CardList;
