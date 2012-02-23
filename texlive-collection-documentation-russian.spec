# revision 13822
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-documentation-russian
Version:	20120223
Release:	1
Summary:	Russian documentation
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-documentation-russian.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-lshort-russian
Requires:	texlive-mpman-ru
Requires:	texlive-texlive-ru
Requires:	texlive-collection-documentation-base

%description
TeXLive collection-documentation-russian package.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
