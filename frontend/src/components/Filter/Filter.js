import './Filter.css';

function Filter({onFilterChange}) {

  function handleFilterChange(e) {
    onFilterChange(e)
  }

  return (
    <label className='filter'>
      <h1 className='filter__title'>Наименование</h1>
      <select className='filter__box' onChange={handleFilterChange}>
        <option value=''>Соответствие</option>
        <option value='all'>Все</option>
        <option value='yes'>Установлено</option>
        <option value='no'>Не установлено</option>
      </select>
      <p className='filter__date'>Дата выгрузки</p>
      <p className='filter__price'>Цена</p>
      <p className='filter__prod-name'>Наименование просепт</p>
    </label>
  )
}

export default Filter;