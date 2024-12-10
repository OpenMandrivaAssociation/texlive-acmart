Name:		texlive-acmart
Version:	72987
Release:	1
Summary:	Class for typesetting publications of ACM
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/acmart
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/acmart.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/acmart.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/acmart.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a class for typesetting publications of
the Association for Computing Machinery (ACM).

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/acmart
%{_texmfdistdir}/tex/latex/acmart
%{_texmfdistdir}/bibtex/bst/acmart
%doc %{_texmfdistdir}/doc/latex/acmart

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
