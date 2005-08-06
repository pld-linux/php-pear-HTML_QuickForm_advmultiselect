%include	/usr/lib/rpm/macros.php
%define		_class		HTML
%define		_subclass	QuickForm
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}_advmultiselect

Summary:	%{_pearname} - element for HTML_QuickForm that emulate a multi-select
Summary(pl):	%{_pearname} - element HTML_QuickForm emuluj±cy wielokrotn± listê wyboru
Name:		php-pear-%{_pearname}
Version:	0.5.1
Release:	1
License:	PHP 3.0
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	f9d0e96e12e0da3432676aaaedb430fd
URL:		http://pear.php.net/package/HTML_QuickForm_advmultiselect/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
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
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/{examples,ChangeLog,NEWS}
%{php_pear_dir}/%{_class}/*.php
