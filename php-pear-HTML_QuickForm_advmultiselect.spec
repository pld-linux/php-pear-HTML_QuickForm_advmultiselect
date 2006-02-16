%include	/usr/lib/rpm/macros.php
%define		_class		HTML
%define		_subclass	QuickForm
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}_advmultiselect

Summary:	%{_pearname} - element for HTML_QuickForm that emulate a multi-select
Summary(pl):	%{_pearname} - element HTML_QuickForm emuluj±cy wielokrotn± listê wyboru
Name:		php-pear-%{_pearname}
Version:	1.1.0
Release:	1
License:	PHP 3.0
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	723082cd3da5e2547323cd4097efc8cc
URL:		http://pear.php.net/package/HTML_QuickForm_advmultiselect/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-common >= 3:4.2.0
Requires:	php-pear
Requires:	php-pear-HTML_Common >= 1.2.1
Requires:	php-pear-HTML_QuickForm > 3.2.4
Requires:	php-pear-PEAR-core
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The HTML_QuickForm_advmultiselect package adds an element to the
HTML_QuickForm package that is two select boxes next to each other
emulating a multi-select.

In PEAR status of this package is: %{_status}.

%description -l pl
Pakiet HTML_QuickForm_advmultiselect rozszerza HTML_QuickForm o dwa
znajduj±ce siê obok siebie pola wyboru emuluj±ce wielokrotn± listê
wyboru.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/{NEWS,ChangeLog,examples,docs/*}
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
