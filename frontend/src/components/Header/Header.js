import './Header.css';
import Logo from '../Logo/Logo';

function Header() {
  return (
    <div className='header'>
      <Logo />
      <div className='header__menu'></div>
    </div>
  );
}

export default Header;