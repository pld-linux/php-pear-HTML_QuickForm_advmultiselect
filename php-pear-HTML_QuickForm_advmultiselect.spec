%include	/usr/lib/rpm/macros.php
%define		_class		HTML
%define		_subclass	QuickForm
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}_advmultiselect

Summary:	%{_pearname} - element for HTML_QuickForm that emulate a multi-select
Summary(pl.UTF-8):	%{_pearname} - element HTML_QuickForm emulujący wielokrotną listę wyboru
Name:		php-pear-%{_pearname}
Version:	1.4.0
Release:	2
License:	PHP 3.0
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	0a240714c786f4916e5e6f481ab8052e
URL:		http://pear.php.net/package/HTML_QuickForm_advmultiselect/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-common >= 3:4.2.0
Requires:	php-pear
Requires:	php-pear-HTML_Common >= 1.2.1
Requires:	php-pear-HTML_QuickForm >= 3.2.4
Requires:	php-pear-PEAR-core >= 1:1.4.3
Conflicts:	php-pear-HTML_QuickForm = 3.2.4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The HTML_QuickForm_advmultiselect package adds an element to the
HTML_QuickForm package that is two select boxes next to each other
emulating a multi-select.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Pakiet HTML_QuickForm_advmultiselect rozszerza HTML_QuickForm o dwa
znajdujące się obok siebie pola wyboru emulujące wielokrotną listę
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
%{php_pear_dir}/data
