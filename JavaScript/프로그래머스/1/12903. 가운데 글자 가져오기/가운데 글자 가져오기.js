const solution = (s) => {
    const l = s.length
    return s.length % 2 !== 0 ? s.slice(Math.floor(l / 2), Math.floor(l / 2) + 1) : s.slice(l / 2 - 1, l / 2 + 1) ;
}