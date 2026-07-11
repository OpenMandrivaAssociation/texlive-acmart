%global tl_name acmart
%global tl_revision 79508

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.19
Release:	%{tl_revision}.1
Summary:	Class for typesetting publications of ACM
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/acmart
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/acmart.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/acmart.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/acmart.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a class for typesetting publications of the
Association for Computing Machinery (ACM).

