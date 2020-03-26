function xout = chop(xin,varargin)
%CHOP(xin,n) truncates the vector xin by n elements, counted from the back
    if isempty(varargin)
        varargin{1} = 1;
    end
    xout = xin(1:end-varargin{1});
end