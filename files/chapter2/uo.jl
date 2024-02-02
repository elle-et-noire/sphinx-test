include("trgutils.jl")

module Potts

function weight(β; q)
  Main.Diagonal([exp(β) - 1 for _ in 1:q]) + ones(q, q)
end

function bulk(β; q)
  Main.bulk(weight(β; q))
end

function horizontalboundary(β; q)
  Main.horizontalboundary(weight(β; q))
end

function criticaltemperature(;q)
  1 / log(1 + √q)
end

end